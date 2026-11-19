from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


async def _alert_headbutt(ctx):
    """Alert Headbutt: base damage 30 against a Pokemon-GX or Pokemon-EX."""
    defender = ctx.defender
    tag = False
    if defender is not None:
        subtypes = [str(s) for s in (getattr(def_for(defender.archetype_id),
                                             "subtypes", None) or [])]
        tag = any(("GX" in s or "EX" in s) for s in subtypes)
    await ctx.deal_damage(30 if tag else 90)

card = PokemonCardDef(
    guid="65803671-e974-5afc-bb81-4769ed0ce4e3",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1", "Gumshoos"],
    subtypes=["Stage 1"],
    collector_number=181,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Attack(
            title="Alert Headbutt",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or Pok\u00e9mon-EX, this attack's base damage is 30.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=_alert_headbutt,
        ),
    ],
)