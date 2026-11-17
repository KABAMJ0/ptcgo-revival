from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37da7e0d-959a-5c72-8bae-41b38ab089fc",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    display_name="Giovanni's Nidoran ♂",
    searchable_by=["Giovanni's Nidoran \u2642", "Basic", "GiovannisNidoran"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Retaliation",
            game_text="You can't use this attack unless Giovanni's Nidoran \u2642 has 2 or more damage counters on it.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)