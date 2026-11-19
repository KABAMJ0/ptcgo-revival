from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_item_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="4b90fb49-1609-5824-b963-3a9047f51590",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic", "Wiglett"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Lucky Find",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(is_item_card, count=1, minimum=1, reveal=True),
        ),
        Attack(
            title="Aqua Bomb",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=recoil_attack(20),
        ),
    ],
)