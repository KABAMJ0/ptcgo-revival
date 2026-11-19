from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="3bbf9764-9f76-5f09-b534-7920c15d9b1c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossandex.Name",
    display_name="Palossand ex",
    searchable_by=["Palossand ex", "Stage 1", "Tera", "ex", "Palossandex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=221,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Barite Jail",
            game_text="Put damage counters on each of your opponent's Benched Pok\u00e9mon until its remaining HP is 100.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
    ],
)