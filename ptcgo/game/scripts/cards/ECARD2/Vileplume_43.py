from ptcgo.game.card_effects.attacks_common import lock_opponent_plays
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb87f0e0-5bcc-58a6-9305-f0e6c3891c92",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Poison Scent",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned and Confused. If tails, the Defending Pok\u00e9mon is now Poisoned and Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Addictive Pollen",
            game_text="Flip a coin. If heads, your opponent can't play Supporter cards during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=lock_opponent_plays("supporter", flip=True),
        ),
    ],
)