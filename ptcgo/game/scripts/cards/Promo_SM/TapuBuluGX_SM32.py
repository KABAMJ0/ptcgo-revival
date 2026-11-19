from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

async def g_max_volt_tackle(ctx):
    energies = ctx.attached_energies(ctx.attacker)
    if energies and await ctx.ask_yes_no(
        "Discard all Energy from this Pokémon? If you do, this attack does 150 more damage."
    ):
        await ctx.discard_energy_from(ctx.attacker, 99)
        await ctx.deal_damage(270)
    else:
        await ctx.deal_damage(120)

card = PokemonCardDef(
    guid="fca83d16-04de-57b4-8e32-fadb7f735bc6",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuBuluGX.Name",
    display_name="Tapu Bulu-GX",
    searchable_by=["Tapu Bulu-GX", "Basic", "GX", "TapuBuluGX"],
    subtypes=["Basic", "GX"],
    collector_number=32,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=787,
    abilities=[
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Nature's Judgment",
            game_text="You may discard all Energy from this Pok\u00e9mon. If you do, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=g_max_volt_tackle,
        ),
        Attack(
            title="Tapu Wilderness-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=heal_attack(all_damage=True, target="self"),
        ),
    ],
)