from ptcgo.game.card_effects.pokemon import energy_provides_type


def is_darkness_energy(card):
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import retaliate_counters_passive

async def dark_slash(ctx):
    """You may discard a Darkness Energy attached to Sharpedo for +30."""
    energies = [card for card in ctx.attached_energies(ctx.attacker)
                if is_darkness_energy(card)]
    bonus = 0
    if energies and await ctx.ask_yes_no(
            "Discard a Darkness Energy from Sharpedo for 30 more damage?"):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 1, predicate=is_darkness_energy,
            prompt="Discard a Darkness Energy card")
        if discarded:
            bonus = 30
    await ctx.deal_damage(70 + bonus)

card = PokemonCardDef(
    guid="c713de78-d71a-5718-8850-543fb3483b56",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If Sharpedo is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Sharpedo is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            passive=retaliate_counters_passive(2),
        ),
        Attack(
            title="Dark Slash",
            game_text="You may discard a Darkness Energy card attached to Sharpedo. If you do, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=dark_slash,
        ),
    ],
)