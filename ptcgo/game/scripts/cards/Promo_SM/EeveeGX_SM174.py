from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard

card = PokemonCardDef(
    guid="3b505fce-184b-5118-83ea-e6be69caccb2",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EeveeGX.Name",
    display_name="Eevee-GX",
    searchable_by=["Eevee-GX", "Basic", "GX", "EeveeGX"],
    subtypes=["Basic", "GX"],
    collector_number=174,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Ascension DNA",
            game_text="Once during your turn (before your attack), if you have a Pok\u00e9mon in your hand that evolves from Eevee, you may put that card onto this Pok\u00e9mon to evolve it. Before evolving, heal all damage from this Pok\u00e9mon. You can't use this Ability during your first turn or on the turn this Pok\u00e9mon was put into play.",
            effect=unimplemented,
        ),
        Attack(
            title="Boost Dash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title="Joy Maker-GX",
            game_text="Put 3 cards from your discard pile into your hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(count=3),
        ),
    ],
)