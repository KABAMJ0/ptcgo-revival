from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _draco_meteor(ctx):
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        results = await ctx.flip_coins(1, "Draco Meteor")
        if results and results[0]:
            await ctx.deal_damage(50, target=pokemon)


async def _draco_meteor(ctx):
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        results = await ctx.flip_coins(1, "Draco Meteor")
        if results and results[0]:
            await ctx.deal_damage(50, target=pokemon)


card = PokemonCardDef(
    guid="3ee89cc3-3935-5393-a219-099cb7e98b67",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Draco Meteor",
            game_text="Flip a coin for each of your opponent's Pok\u00e9mon. If that coin flip is heads, this attack does 50 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            effect=_draco_meteor,
        ),
    ],
)