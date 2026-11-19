from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from ptcgo.game.card_effects.attacks_common import damage_per, count_discard
from ptcgo.game.session.effects import is_pokemon_card

async def axe_break(ctx):
    """120 damage; also 60 to 1 opposing Benched Pokemon V (no W/R)."""
    await ctx.deal_damage()
    bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon V"
        )
        if target is not None:
            await ctx.deal_damage(60, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="d4c76c5a-932f-5200-8390-2ae28f998560",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVSTAR.Name",
    display_name="Deoxys VSTAR",
    searchable_by=["Deoxys VSTAR", "VSTAR", "DeoxysVSTAR"],
    subtypes=["VSTAR"],
    collector_number=46,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Attack(
            title="Psychic Javelin",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon V. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=axe_break,
        ),
        Attack(
            title="Star Force",
            game_text="This attack does 60 damage for each Energy attached to both Active Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)