from ptcgo.game.card_effects.passives_common import play_lock_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5323c457-31cb-55d4-aad6-c24a4b528ff3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplumeex.Name",
    display_name="Vileplume ex",
    searchable_by=["Vileplume ex", "Stage 2", "ex", "Vileplumeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=100,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Block Dust",
            game_text="As long as Vileplume ex is your Active Pok\u00e9mon, your opponent can't play any Trainer cards (except for Supporter cards) from his or her hand.",
            passive=play_lock_passive("trainer", excluding="supporter"),
        ),
        Attack(
            title="Special Formula",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep and Poisoned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)