from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a5dea72b-db8c-5b46-9c64-2209c493f5b5",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Gather the Crew",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=1),
        ),
        Attack(
            title="Rage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=30),
        ),
    ],
)