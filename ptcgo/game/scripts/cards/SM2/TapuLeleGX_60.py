from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b95990f8-b700-53f7-9345-d39287089c84",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuLeleGX.Name",
    display_name="Tapu Lele-GX",
    searchable_by=["Tapu Lele-GX", "Basic", "GX", "TapuLeleGX"],
    subtypes=["Basic", "GX"],
    collector_number=60,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=786,
    abilities=[
        Ability(
            title="Wonder Tag",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(predicate=is_supporter_card, count=1),
        ),
        Attack(
            title="Energy Drive",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Tapu Cure-GX",
            game_text="Heal all damage from 2 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)