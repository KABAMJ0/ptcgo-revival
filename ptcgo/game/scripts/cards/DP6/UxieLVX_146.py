from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _zen_blade(ctx):
    """Zen Blade: this attack is locked for the user's next turn."""
    await ctx.deal_damage()
    ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                       ctx.ability.ability_id)

card = PokemonCardDef(
    guid="43a80b44-06c4-5852-9e6d-54a88b03d0cf",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UxieLVX.Name",
    display_name="Uxie LV.X",
    searchable_by=["Uxie LV.X", "Level-Up", "UxieLVX"],
    subtypes=["Level-Up"],
    collector_number=146,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    family_id=480,
    abilities=[
        Ability(
            title="Trade Off",
            game_text="Once during your turn (before your attack), you may look at the top 2 cards of your deck, choose 1 of them, and put it into your hand. Put the other card on the bottom of your deck. This power can't be used if Uxie is affected by a Special Condition. You can't use more than 1 Trade Off Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Trade Off",
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(
                AttrID.SPECIAL_CONDITIONS),
            effect=look_at_top(2, take=1, rest="bottom"),
        ),
        Attack(
            title="Zen Blade",
            game_text="Uxie can't use Zen Blade during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_zen_blade,
        ),
    ],
)