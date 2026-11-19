from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _eruption(ctx):
    milled = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, pid)
        if top:
            await ctx.discard_cards(top)
            milled.extend(top)
    await ctx.deal_damage(20 * sum(1 for card in milled if is_energy_card(card)))

card = PokemonCardDef(
    guid="892f5321-9cf1-56aa-98ed-73f5597ddedb",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 20 damage times the number of Energy cards discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="x",
            effect=_eruption,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
