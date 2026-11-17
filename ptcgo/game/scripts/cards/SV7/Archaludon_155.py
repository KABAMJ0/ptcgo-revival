from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a31d21fe-a542-5cc7-a901-a940c462f80e",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludon.Name",
    display_name="Archaludon",
    searchable_by=["Archaludon", "Stage 1", "Archaludon"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Metal Bridge",
            game_text="All of your Pok\u00e9mon that have Metal Energy attached have no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Iron Blaster",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)