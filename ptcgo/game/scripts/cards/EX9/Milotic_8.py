from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="bb1cce4c-403e-5b54-9386-195c0d994725",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Super Hypno Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)