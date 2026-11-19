from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5fba4b1b-fc09-54c5-9e3a-e2c92968a90d",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    display_name="Tyrunt",
    searchable_by=["Tyrunt", "Stage 1", "Tyrunt"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)