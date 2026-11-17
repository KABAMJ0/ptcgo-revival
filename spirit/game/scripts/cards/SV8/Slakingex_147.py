from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e741fa2-6015-57c7-b249-7b816c90f5a9",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakingex.Name",
    display_name="Slaking ex",
    searchable_by=["Slaking ex", "Stage 2", "ex", "Slakingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=147,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Born to Slack",
            game_text="If your opponent has no Pok\u00e9mon ex or Pok\u00e9mon V in play, this Pok\u00e9mon can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Great Swing",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=280,
            effect=unimplemented,
        ),
    ],
)