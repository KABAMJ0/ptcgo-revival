from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

card = PokemonCardDef(
    guid="5d5cce3a-1554-5b87-a493-7fb2b226bea6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkEspeon.Name",
    display_name="Dark Espeon",
    searchable_by=["Dark Espeon", "Stage 1", "DarkEspeon"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=196,
    abilities=[
        Attack(
            title="Gouge",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_choice(heads=20, tails=10),
        ),
        Attack(
            title="Psysplash",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon for each Energy card attached to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)