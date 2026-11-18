from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import all_of, named_exactly

card = PokemonCardDef(
    guid="7d897483-330e-5884-b2e4-a589b91825b0",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♀",
    searchable_by=["Nidoran \u2640", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=29,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon card named Nidoran \u2640 or Nidoran \u2642 and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(all_of(is_basic_pokemon, named_exactly("nidoran")), count=1),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)