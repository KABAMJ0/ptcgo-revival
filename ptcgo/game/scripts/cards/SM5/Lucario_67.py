from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import requires_in_play, search_to_hand


def _is_garchomp(pokemon) -> bool:
    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Garchomp"

card = PokemonCardDef(
    guid="2f52a45a-a088-5d7a-a390-535f5a69fb53",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SM5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=448,
    abilities=[
        Ability(
            title="Precognitive Aura",
            game_text="Once during your turn (before your attack), if you have Garchomp in play, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=search_to_hand(),
            condition=requires_in_play(_is_garchomp),
        ),
        Attack(
            title="Missile Jab",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)