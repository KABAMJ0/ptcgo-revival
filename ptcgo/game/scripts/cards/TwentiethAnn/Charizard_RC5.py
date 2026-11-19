from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.session.passives import previous_evolution_attacks


async def recall(ctx):
    attacks = previous_evolution_attacks(ctx.attacker)
    if not attacks:
        return
    picked = await ctx.choose_attack_to_copy(
        [(ctx.attacker, attack) for attack in attacks],
        "Choose an attack from this Pokemon's previous Evolutions")
    if picked is None:
        return
    _source, chosen = picked
    await ctx.use_attack(chosen)

card = PokemonCardDef(
    guid="531bd232-1509-589e-9c78-268e42227539",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=10005,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Recall",
            game_text="Choose 1 of this Pok\u00e9mon's attacks from its previous Evolutions and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recall,
        ),
        Attack(
            title="Combustion Blast",
            game_text="This Pok\u00e9mon can't use Combustion Blast during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)