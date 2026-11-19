from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.pokemon import energy_provides_type
async def recover(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.WATER.value),
        prompt="Discard 1 Water Energy card attached to Starmie")
    if not discarded:
        return
    pokemon = ctx.attacker
    missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
    if missing > 0:
        await ctx.heal(missing, pokemon)


card = PokemonCardDef(
    guid="4b3a9442-b110-55c4-aa05-7858b3d2ae8d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard 1 Water Energy card attached to Starmie in order to use this attack. Remove all damage counters from Starmie.",
            cost={PokemonTypes.WATER: 2},
            effect=recover,
        ),
        Attack(
            title="Star Freeze",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)