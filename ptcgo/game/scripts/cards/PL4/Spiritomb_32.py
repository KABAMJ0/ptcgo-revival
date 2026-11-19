from ptcgo.game.card_effects.passives_common import play_lock_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01e17d1b-f8ea-5739-bca6-dbaa26771d29",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=442,
    abilities=[
        Ability(
            title="Keystone Seal",
            game_text="As long as Spiritomb is your Active Pok\u00e9mon, each player can't play any Trainer cards from his or her hand.",
            passive=play_lock_passive("trainer", opponents_only=False),
        ),
        Attack(
            title="Darkness Grace",
            game_text="Search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) If you do, put 1 damage counter on Spiritomb. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Will-o'-the-wisp",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)