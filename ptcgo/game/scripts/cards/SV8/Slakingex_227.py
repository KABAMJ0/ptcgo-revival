from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="6b31d573-8438-5c24-bc1c-2e861798ae3a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakingex.Name",
    display_name="Slaking ex",
    searchable_by=["Slaking ex", "Stage 2", "ex", "Slakingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=227,
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
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)