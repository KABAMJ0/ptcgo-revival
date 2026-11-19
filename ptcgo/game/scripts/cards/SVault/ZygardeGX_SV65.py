from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import has_rule_box


async def verdict_gx(ctx):
    """Printed 150, then no damage from Pokemon-GX/EX attacks next turn."""
    await ctx.deal_damage()
    from ptcgo.game.card_effects.passives_common import apply_protection
    await apply_protection(
        ctx, target=ctx.attacker, prevent=True,
        attacker_pred=lambda attacker: has_rule_box(attacker.archetype_id))

card = PokemonCardDef(
    guid="effdb2a2-399b-5c8c-8c3d-80f3e047514b",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name",
    display_name="Zygarde-GX",
    searchable_by=["Zygarde-GX", "Basic", "GX", "ZygardeGX"],
    subtypes=["Basic", "GX"],
    collector_number=65,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Cell Connector",
            game_text="Attach 2 Fighting Energy cards from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=attach_from_discard(basic_energy_of("fighting"), count=2, minimum=0, target="self"),
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
        Attack(
            title="Verdict-GX",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon-GX and Pok\u00e9mon-EX during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=verdict_gx,
        ),
    ],
)