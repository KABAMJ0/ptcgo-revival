from ptcgo.game.card_effects.attacks_common import lock_opponent_plays
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4281dbcc-37a0-58b9-a450-65f194b2d1f8",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Headache",
            game_text="Flip a coin. If heads, your opponent can't play any Trainer, Supporter, or Stadium cards from his or her hand during his or her next turn.",
            cost={},
            effect=lock_opponent_plays("trainer", "supporter", "stadium", flip=True),
        ),
        Attack(
            title="Latent Power",
            game_text="Flip a coin. If tails, this attack does no damage to the Defending Pok\u00e9mon. Instead, Psyduck is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)