from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="762bf41f-7a8e-5c31-9435-ef5eeaa187bd",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Fragile Husk",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon ex, your opponent can't take any Prize cards for it.",
            effect=unimplemented,
        ),
        Attack(
            title="Damage Beat",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)