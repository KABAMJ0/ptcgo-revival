from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import all_of, named_exactly

card = PokemonCardDef(
    guid="aac1a720-4b2b-55f3-8b65-76cb56c0b567",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    display_name="Krabby",
    searchable_by=["Krabby", "Basic", "Krabby"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=98,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon named Krabby and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench if full.)",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_bench(all_of(is_basic_pokemon, named_exactly("krabby")), count=1),
        ),
        Attack(
            title="Irongrip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)