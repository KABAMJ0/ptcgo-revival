from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="f64ed985-54ae-59da-a038-6cc93e1c9520",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=7,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)