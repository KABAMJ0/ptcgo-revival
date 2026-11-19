from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of, is_tool_card

async def _plunder(ctx):
    """10 damage, after discarding the Trainer cards attached to the Defending
    Pokemon (text order: the discard happens before the damage)."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        attached = [c for c in defender.children if is_tool_card(c)]
        if attached:
            await ctx.discard_cards(attached)
    await ctx.deal_damage()


card = PokemonToolCardDef(
    guid="ebdc4f65-897f-548f-9d54-8deab3d4aabc",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarknessCube01.Name",
    display_name="Darkness Cube 01",
    searchable_by=["Darkness Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=119,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Plunder",
            game_text="Before doing damage, discard any Trainer cards attached "
                      "to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=_plunder,
        ),
        Ability(
            title="Darkness Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("darkness"),
)
