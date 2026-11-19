from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="2f959b67-c000-5c02-8e79-f3698f563f10",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    display_name="Numel",
    searchable_by=["Numel", "Basic", "Numel"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=322,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)