from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import attack_discount_passive
from ptcgo.game.content.definitions import evolves_from


def _eevee_gx(pokemon) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return ("GX" in (getattr(definition, "subtypes", None) or [])
            and evolves_from(pokemon.archetype_id, "Eevee"))

card = PokemonCardDef(
    guid="4383f2f1-5a59-5686-99a9-3fe5487bfbe7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Speed Cheer",
            game_text="The attacks of your Pok\u00e9mon-GX in play that evolve from Eevee cost Colorless less. You can't apply more than 1 Speed Cheer Ability at a time.",
            passive=attack_discount_passive(1, self_only=False, pred=_eevee_gx),
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)