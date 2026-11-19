from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _typed(energies, type_value):
    return [energy for energy in energies
            if energy_provides_type(energy, type_value)]


async def _white_hot_flame(ctx):
    attacker = ctx.attacker
    if attacker is None:
        return
    attached = ctx.attached_energies(attacker)
    fire = _typed(attached, PokemonTypes.FIRE.value)
    bolt = _typed(attached, PokemonTypes.LIGHTNING.value)
    if not fire or not bolt:
        return  # "or this attack does nothing"
    await ctx.discard_cards([fire[0], bolt[0]])
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "White-hot Flame")
    if not (results and results[0]):
        await ctx.deal_damage(30, target=attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="3d41f97e-f76c-53e7-a980-3f5d25b6fe4e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCharizard.Name",
    display_name="Shining Charizard",
    searchable_by=["Shining Charizard", "Basic", "ShiningCharizard"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=6,
    abilities=[
        Attack(
            title="White-hot Flame",
            game_text="Discard 1 Fire Energy card and 1 Lightning Energy card attached to Shining Charizard or this attack does nothing. Flip a coin. If tails, Shining Charizard does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=_white_hot_flame,
        ),
    ],
)