from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon


card = PokemonCardDef(
    guid="8dcbb35f-27d6-5f08-9061-fac4d60106f0",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    display_name="Pansage",
    searchable_by=["Pansage", "Basic", "Pansage"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=511,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic_pokemon, count=1),
        ),
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=heal_attack(10),
        ),
    ],
)