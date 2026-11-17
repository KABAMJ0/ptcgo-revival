from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db93e36c-7059-58db-9d8f-afcff219d433",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsTrevenant.Name",
    display_name="Hop's Trevenant",
    searchable_by=["Hop's Trevenant", "Stage 1", "HopsTrevenant"],
    subtypes=["Stage 1"],
    collector_number=237,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPhantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Horrifying Revenge",
            game_text="If any of your Hop's Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)