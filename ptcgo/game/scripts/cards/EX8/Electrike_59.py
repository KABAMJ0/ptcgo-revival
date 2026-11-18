from ptcgo.game.card_effects.attacks_common import lock_opponent_plays
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d65fe02f-7bab-5eb1-a554-0ad891fddc9e",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    display_name="Electrike",
    searchable_by=["Electrike", "Basic", "Electrike"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=309,
    abilities=[
        Attack(
            title="High Voltage",
            game_text="Flip a coin. If heads, your opponent can't play Trainer cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=lock_opponent_plays("trainer", damage=0, flip=True),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
