from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="1dba69cb-1dcb-5ac6-a217-9a0911f47ff8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    display_name="Sinistea",
    searchable_by=["Sinistea", "Basic", "Sinistea"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=854,
    abilities=[
        Attack(
            title="Cold Tea",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)