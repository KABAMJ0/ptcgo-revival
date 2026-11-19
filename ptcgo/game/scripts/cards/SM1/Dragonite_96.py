from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _dragon_wave(ctx):
    for type_value in (PokemonTypes.GRASS.value, PokemonTypes.LIGHTNING.value):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card: energy_provides_type(card, type_value),
            prompt="Choose the Energy to discard from this Pok\u00e9mon")
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b33a1582-e923-532f-bb0a-37d4e3150744",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Dragon Wave",
            game_text="Discard a Grass Energy and a Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1},
            damage=130,
            effect=_dragon_wave,
        ),
        Attack(
            title="Giant Tail",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=200,
            effect=flip_or_nothing(),
        ),
    ],
)