from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _lightning_strike(ctx):
    lightning = [e for e in ctx.attached_energies(ctx.attacker) if _is_lightning(e)]
    if lightning and await ctx.ask_yes_no(
            "Do 40 damage plus 60 more damage and discard all Lightning Energy?"):
        await ctx.deal_damage(100)
        await ctx.discard_cards(lightning)
        return
    await ctx.deal_damage(40)

card = PokemonCardDef(
    guid="49411d01-efc6-5844-9003-f421b1c8cf00",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may do 40 damage plus 60 more damage. If you do, discard all Lightning Energy attached to Electrode.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=_lightning_strike,
        ),
    ],
)
