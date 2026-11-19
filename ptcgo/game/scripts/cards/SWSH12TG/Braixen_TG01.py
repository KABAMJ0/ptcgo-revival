from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_discard


def _is_serena_card(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Serena"


card = PokemonCardDef(
    guid="ed793162-1d5b-51ae-a31b-ab4088b1bdfb",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    display_name="Braixen",
    searchable_by=["Braixen", "Stage 1", "Braixen"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="SWSH12TG",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Flare Parade",
            game_text="This attack does 60 damage for each Serena card in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_discard("mine", _is_serena_card), 60),
        ),
    ],
)
