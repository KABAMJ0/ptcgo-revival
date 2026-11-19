from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="9cf4224e-3b7e-5ba4-8f61-6ebf4da81ad1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1", "Krokorok"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=no_retreat_attack(),
        ),
    ],
)