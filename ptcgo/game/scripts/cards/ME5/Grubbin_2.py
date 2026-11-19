from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="5ae1bb6d-4180-5c7f-b912-e5b014121fe6",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    display_name="Grubbin",
    searchable_by=["Grubbin", "Basic", "Grubbin"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=736,
    abilities=[
        Attack(
            title="String Shot",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)