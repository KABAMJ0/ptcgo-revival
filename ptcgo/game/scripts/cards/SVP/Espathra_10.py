from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7904a30e-e06b-5801-8e99-1beb08b2b15e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1", "Espathra"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=956,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)