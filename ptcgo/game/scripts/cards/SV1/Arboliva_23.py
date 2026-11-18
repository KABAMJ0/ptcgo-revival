from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_all_from_one

_heal_one = heal_all_from_one()


async def _enriching_oil(ctx):
    """On evolve: you may heal all damage from 1 of your Pokemon."""
    if not await ctx.ask_yes_no("Heal all damage from 1 of your Pokémon?"):
        return
    await _heal_one(ctx)

card = PokemonCardDef(
    guid="ab6584ad-f5f2-5778-ad46-3912fc65cd68",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2", "Arboliva"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Ability(
            title="Enriching Oil",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may heal all damage from 1 of your Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_enriching_oil,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)