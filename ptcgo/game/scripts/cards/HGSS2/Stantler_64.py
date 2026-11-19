from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="d5f63fe7-06b4-594e-9cd7-9825f56b899e",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Mystifying Horns",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)