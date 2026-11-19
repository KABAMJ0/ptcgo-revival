from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.session.effects import full_stack


async def _frost_vanish(ctx):
    """Printed 40; you may take this Pokemon and everything under it back
    into your hand."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    if attacker is None:
        return
    await ctx.put_in_hand(full_stack(attacker), reveal=False)


card = PokemonCardDef(
    guid="7f8c299a-09ef-5aeb-9550-bed55bbc9f82",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Cryogonal"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Ice Chain",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=gust_attack(damage_to_new_active=0),
        ),
        Attack(
            title="Frost Vanish",
            game_text="You may return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=_frost_vanish,
        ),
    ],
)