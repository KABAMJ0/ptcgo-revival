from ptcgo.game.card_effects.attacks_common import bonus_if, defender_is_evolved
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="883606c4-e5bd-5073-8c94-43e96d581c54",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeSnorlaxGX.Name",
    display_name="Eevee & Snorlax-GX",
    searchable_by=["Eevee & Snorlax-GX", "Basic", "TAG TEAM", "GX", "EeveeSnorlaxGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=169,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Attach an Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_hand(is_basic_energy_card, count=1, target='choice'),
        ),
        Attack(
            title="Dump Truck Press",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=bonus_if(defender_is_evolved, 120),
        ),
        Attack(
            title="Megaton Friends-GX",
            game_text="If this Pok\u00e9mon has at least 1 extra Energy attached to it (in addition to this attack's cost), draw cards until you have 10 cards in your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=210,
            effect=unimplemented,
        ),
    ],
)