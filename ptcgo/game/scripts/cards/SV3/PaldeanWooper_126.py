from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="588f207c-9724-58da-bd9d-fb8dae5fcf75",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    display_name="Paldean Wooper",
    searchable_by=["Paldean Wooper", "Basic", "PaldeanWooper"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=194,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)