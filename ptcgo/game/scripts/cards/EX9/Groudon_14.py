from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_energy_card

async def eruption(ctx):
    discarded = []
    for player_id in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, player_id=player_id)
        if top:
            discarded.extend(top)
    if not discarded:
        return
    await ctx.discard_cards(discarded)
    energy = sum(1 for card in discarded if is_energy_card(card))
    amount = 40 + 10 * energy
    await ctx.deal_damage(amount)

card = PokemonCardDef(
    guid="8248a2de-6179-589f-abd3-9e7b8191922e",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 40 damage plus 10 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=eruption,
        ),
    ],
)