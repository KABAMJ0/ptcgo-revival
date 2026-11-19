from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _illumise_in_play(ctx) -> bool:
    for pokemon in ctx.my_pokemon_in_play():
        definition = def_for(getattr(pokemon, "archetype_id", "") or "")
        if definition is not None and (definition.display_name or "") == "Illumise":
            return True
    return False


async def _illumisile(ctx):
    if not _illumise_in_play(ctx):
        return
    await snipe_attack(30, pool="bench", count=1, apply_modifiers=False)(ctx)

card = PokemonCardDef(
    guid="38c3ba15-9efe-54c8-9c66-b51420ffdecc",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name",
    display_name="Volbeat",
    searchable_by=["Volbeat", "Basic", "Volbeat"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=313,
    abilities=[
        Attack(
            title="Illumisile",
            game_text="If you don't have Illumise in play, this attack does nothing. Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=_illumisile,
        ),
        Attack(
            title="Firefly Light",
            game_text="The Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
