from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18ada343-4fae-5009-b63a-dfea89075e46",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    display_name="Marshtomp",
    searchable_by=["Marshtomp", "Stage 1", "Marshtomp"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Natural Cure",
            game_text="When you attach a Water Energy card from your hand to Marshtomp, remove all Special Conditions from Marshtomp.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)