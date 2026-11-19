from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.support_common import draw_attack


def _tools_in_play(ctx) -> int:
    """Pokemon Tools attached to every Pokemon in play, both sides."""
    return len(ctx.tools_in_play())


card = PokemonCardDef(
    guid="202b7cc6-4995-5c86-a547-5fb88e27e0db",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Tool Drop",
            game_text="This attack does 40 damage for each Pok\u00e9mon Tool attached to all Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="x",
            effect=damage_per(_tools_in_play, 40),
        ),
    ],
)